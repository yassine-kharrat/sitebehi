from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Scenario
from .serializers import ScenarioSerializer

class ScenarioView(APIView):
    def get(self, request):
        scenarios = Scenario.objects.all()
        serializer = ScenarioSerializer(scenarios, many=True)
        return Response(serializer.data)

class FeedbackView(APIView):
    def post(self, request):
        data = request.data
        scenario_id = data.get("scenario_id")
        player_choice = data.get("choice")

        scenario = Scenario.objects.get(id=scenario_id)
        correct_answers = scenario.correct_answers

        if player_choice in correct_answers:
            feedback = "Great choice! This aligns well with best practices."
        else:
            feedback = "This might not be the best choice. Consider other factors."

        return Response({"feedback": feedback})
