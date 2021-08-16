from django.urls import path
from polls import class_views


urlpatterns = [
    path("poll-class-view/", class_views.PollView.as_view(), name="poll-class-view"),
    path("question-class-view/", class_views.QuestionView.as_view(), name="question-class-view"),
    path("answer-class-view/", class_views.AnswerView.as_view(), name="answer-class-view"),
    path("poll2-form-view/", class_views.PollFormView.as_view(), name="poll2-form-view"),
    path("question2-form-view/", class_views.QuestionFormView.as_view(), name="question2-form-view"),
    path("answer2-form-view/", class_views.AnswerFormView.as_view(), name="answer2-form-view"),
    path("my-question-detail-view/<pk>/", class_views.QuestionDetailView.as_view(), name="my-question-detail-view"),
    path("my-poll-detail-view/<pk>/", class_views.PollDetailView.as_view(), name="my-poll-detail-view"),
    path("my-answer-detail-view/<pk>/", class_views.AnswerDetailView.as_view(), name="my-answer-detail-view"),
    path("my-question-update-view/<pk>/", class_views.QuestionUpdateView.as_view(), name="my-question-update-view"),
    path("my-answer-update-view/<pk>/", class_views.AnswerUpdateView.as_view(), name="my-answer-update-view"),
    path("my-poll-update-view/<pk>/", class_views.PollUpdateView.as_view(), name="my-poll-update-view"),
    path("my-question-delete-view/<pk>/", class_views.QuestionDeleteView.as_view(), name="my-question-delete-view"),
    path("my-answer-delete-view/<pk>/", class_views.AnswerDeleteView.as_view(), name="my-answer-delete-view"),
    path("my-poll-delete-view/<pk>/", class_views.PollDeleteView.as_view(), name="my-poll-delete-view")
]