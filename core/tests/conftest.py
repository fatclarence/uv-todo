# helpers for tests

import pytest
from model_bakery import baker

# django_user_model is a built-in pytest fixture provided by pytest-django 
# that gives you access to the active User model in your Django project.
# 
# The django_user_model value is "captured" at fixture creation time
# Creates a new instance each time with different params
@pytest.fixture
def make_user(django_user_model):
  def _make_user(**kwargs):
    return baker.make(django_user_model, **kwargs)
  return _make_user

@pytest.fixture
def make_todo(make_user):
  def _make_todo(user=None,**kwargs):
    return baker.make("core.Todo", user=user or make_user(), **kwargs)
  return _make_todo
