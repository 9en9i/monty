import pytest


def test_list_books(client):
    response = client.get("/book")
    assert response.status_code == 200
    assert response.text == "List book"


@pytest.mark.parametrize("book_id, response_text", (
        (0, "Retrieve book: 0"),
        (1, "Retrieve book: 1"),
        (2, "Retrieve book: 2"),
))
def test_retrieve_book(client, book_id, response_text):
    response = client.get(f"/book/{book_id}")
    assert response.status_code == 200
    assert response.text == response_text

