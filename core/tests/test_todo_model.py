# from django.test import TestCase
import pytest

@pytest.mark.django_db
class TestTodo:
  def test_todo_association_with_users(self, make_user, make_todo):
    [user1, user2] = make_user(_quantity=2)

    for i in range(3):
      make_todo(user=user1, title=f"Todo {i} for user 1")
    
    make_todo(user=user2, title="Todo for user 2")

    assert user1.todos.count() == 3
    assert {todo.title for todo in user1.todos.all()} == {
      f"Todo {i} for user 1" for i in range(3)
    }

    assert user2.todos.count() == 1
    assert { todo.title for todo in user2.todos.all() } == {"Todo for user 2"}
