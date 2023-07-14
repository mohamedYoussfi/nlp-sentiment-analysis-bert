import tensorflow as tf
from django.http import JsonResponse
from rest_framework.decorators import api_view
import tensorflow_text as text
import numpy as np
from deep_translator import GoogleTranslator

translator = GoogleTranslator()
"""
tf.saved_model.LoadOptions(
    allow_partial_checkpoint=False,
    experimental_io_device=None,
    experimental_skip_checkpoint=False,
    experimental_variable_policy=None,
)
"""

model = tf.keras.models.load_model("sentiment-analysis")


@api_view(["GET"])
def test(request):
    review = request.query_params.get("review")
    review_translated = translator.translate(review)
    result = model.predict([review_translated])
    result = np.where(result > 0.5, 1, 0)
    data = {
        "name": "sentiment analysis",
        "review": review,
        "review_trans": review_translated,
        "result": str(result[0][0]),
    }
    return JsonResponse(data)
