
from pgit.core.comparator import compare_results
from pgit.core.results import TestResult as EvaluationResult


def test_unchanged_result():
    baseline = [EvaluationResult("1", "Refund policy", True)]
    current = [EvaluationResult("1", "Refund policy", True)]

    assert compare_results(baseline, current) == [
        ("Refund policy", "UNCHANGED")
    ]


def test_regressed_result():
    baseline = [EvaluationResult("1", "Refund policy", True)]
    current = [EvaluationResult("1", "Refund policy", False)]

    assert compare_results(baseline, current) == [
        ("Refund policy", "REGRESSED")
    ]


def test_improved_result():
    baseline = [EvaluationResult("1", "Uncertainty", False)]
    current = [EvaluationResult("1", "Uncertainty", True)]

    assert compare_results(baseline, current) == [
        ("Uncertainty", "IMPROVED")
    ]


def test_new_result():
    baseline = []
    current = [EvaluationResult("2", "New evaluation", True)]

    assert compare_results(baseline, current) == [
        ("New evaluation", "NEW")
    ]


def test_removed_result():
    baseline = [EvaluationResult("1", "Refund policy", True)]
    current = []

    assert compare_results(baseline, current) == [
        ("Refund policy", "REMOVED")
    ]
