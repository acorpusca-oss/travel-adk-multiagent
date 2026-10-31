from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_cusco():
    result = get_local_culture_info("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["dishes"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["phrases"]) >= 1


def test_get_local_culture_info_accent_and_case():
    result = get_local_culture_info("  PARÍS ")

    assert result["status"] == "success"
    assert any("Bonjour" in phrase for phrase in result["phrases"])


def test_get_local_culture_info_not_found():
    result = get_local_culture_info("Atlantis")

    assert result["status"] == "not_found"
    assert "message" in result


def test_get_local_culture_info_empty_destination():
    result = get_local_culture_info("   ")

    assert result["status"] == "error"
    assert "destination" in result["message"].lower()
