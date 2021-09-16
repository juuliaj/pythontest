import postinumerot

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST"
}

def test_postitoimipaikka_loytyy(mocker):
    data = POSTINUMEROT
    mocker.patch('http_pyynto.hae_postinumerot', return_value=data)

    tulos = postinumerot.etsi_postinumerot('JUUPAJOKI')

    assert tulos == '35540'


def test_kiuruvesi_postinumerot(mocker):
    data = POSTINUMEROT
    mocker.patch('http_pyynto.hae_postinumerot', return_value=data)

    tulos = postinumerot.etsi_postinumerot('KIURUVESI')

    assert tulos == '74700, 74701'


def test_bug_is_real(mocker):
    data = ERIKOISTAPAUKSET
    mocker.patch('http_pyynto.hae_postinumerot', return_value=data)

    tulos = postinumerot.etsi_postinumerot('SMART POST')

    assert tulos == '65374, 74704'