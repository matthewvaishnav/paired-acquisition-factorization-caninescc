"""Minimal model namespace for the external canine SCC Paired-Acquisition Neural Factorization study."""

from .scorpion_paired_acquisition_factorization import (
    ProjectionConfig,
    ScorpionProjection,
    projection_loss,
)

__all__ = [
    "ProjectionConfig",
    "ScorpionProjection",
    "projection_loss",
]
