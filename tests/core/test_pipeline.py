import pytest

from core.context import ReconContext
from core.pipeline import ReconPipeline
from modules.base import ReconModule


class DummyModule(ReconModule):
    """
    Minimal valid recon module for testing the pipeline.
    """
    name = "dummy"

    def run(self, context: ReconContext) -> None:
        context.metadata["dummy_executed"] = True


def test_pipeline_executes_module_and_updates_context():
    """
    Pipeline should execute modules sequentially
    and allow them to mutate the context.
    """
    context = ReconContext(target="example.com")
    pipeline = ReconPipeline(modules=[DummyModule()])

    result = pipeline.run(context)

    assert result.metadata["dummy_executed"] is True


def test_pipeline_rejects_non_recon_module():
    """
    Pipeline must raise TypeError if an invalid
    module is passed.
    """
    context = ReconContext(target="example.com")
    pipeline = ReconPipeline(modules=[object()])

    with pytest.raises(TypeError):
        pipeline.run(context)
