
import json

from pgit.core import storage
from pgit.core.results import TestResult as EvaluationResult


def test_save_and_load_results(tmp_path, monkeypatch):
    results_file = tmp_path / "results.json"
    monkeypatch.setattr(storage, "RESULTS_FILE", results_file)

    original = [
        EvaluationResult("1", "Refund policy", True),
        EvaluationResult("2", "Uncertainty", False),
    ]

    storage.save_results(original)
    loaded = storage.load_results()

    assert loaded == original


def test_save_and_load_baseline(tmp_path, monkeypatch):
    baseline_file = tmp_path / "baseline.json"
    monkeypatch.setattr(storage, "BASELINE_FILE", baseline_file)

    original = [
        EvaluationResult("1", "Refund policy", True),
    ]

    storage.save_baseline(original)
    loaded = storage.load_baseline()

    assert loaded == original


def test_missing_file_returns_empty_list(tmp_path, monkeypatch):
    missing_file = tmp_path / "missing.json"
    monkeypatch.setattr(storage, "RESULTS_FILE", missing_file)

    assert storage.load_results() == []


def test_saved_results_are_valid_json(tmp_path, monkeypatch):
    results_file = tmp_path / "results.json"
    monkeypatch.setattr(storage, "RESULTS_FILE", results_file)

    storage.save_results([
        EvaluationResult("1", "Refund policy", True),
    ])

    data = json.loads(results_file.read_text(encoding="utf-8"))

    assert data[0]["id"] == "1"
    assert data[0]["name"] == "Refund policy"
    assert data[0]["passed"] is True
