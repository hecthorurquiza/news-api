from .feeling_model_handler import FeelingModelHandler

def test_analyze_feeling():
	handler = FeelingModelHandler()
	result = handler.analyze_feeling("I'm excited to share my last contribution to the project!")

	assert result is not None
	assert result["label"] is not None
	assert result["score"] is not None
	assert result["score"] > 0.0
    