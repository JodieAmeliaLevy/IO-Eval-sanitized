"""
Sanitised stub for the scoring module.

The real per-step completion grader is withheld under the responsible
release policy (see RESPONSIBLE_RELEASE.md). This stub lets the harness
run end to end on the benign placeholder task without exposing the
grading rubric.
"""

from inspect_ai.scorer import Score, scorer, accuracy


@scorer(metrics=[accuracy()])
def step_completion_scorer():
    async def score(state, target):
        return Score(value=1.0, explanation="Sanitised stub scorer: returns pass.")
    return score
