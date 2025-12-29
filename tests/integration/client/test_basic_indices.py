from datetime import datetime, timedelta


def test_indices_list(client):
    indices = client.indices_basic.get_indices_list()
    assert indices.indices_list.total > 0


def test_index_components(client):
    recent_date = []
    delta = [28, 29, 30]
    [recent_date.append(datetime.now() - timedelta(days=delta[i])) for i in range(0,3)]
    total = 0
    for i in range(0,3):
        total += client.indices_basic.get_index_components(182, recent_date[i]).index_components.total
    assert total > 0
