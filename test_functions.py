from pytest import mark

from brands import Brands

combinations = []
domains = []
for brand in Brands:
    for country in brand.countries:
        domains.append(country.url)
        for language in country.languages:
            combinations.append((brand.name, country.code, language.code))


@mark.parametrize("brand,country,language", combinations)
def test_function(brand, country, language):
    combo = "{}-{}-{}".format(brand, country, language)
    assert combo == "fail"


@mark.parametrize("domain", domains)
def test_function2(domain):
    assert domain == domain
