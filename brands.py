from collections import namedtuple

Brand = namedtuple("Brand", "name countries")
BrandCountry = namedtuple("BrandCountry", "code languages url basic_auth")
Lang = namedtuple("Lang", "code")

BrandA = Brand(
    name="brandA",
    countries=[
        BrandCountry(
            code="DE",
            languages=[
                Lang("de")
            ],
            url="mona.de",
            basic_auth=False
        ),
        BrandCountry(
            code="BE",
            languages=[
                Lang("nl"),
                Lang("fr")
            ],
            url="brand.be.localhost",
            basic_auth=True
        )
    ]
)

BrandB = Brand(
    name="brandB",
    countries=[
        BrandCountry(
            code="DE",
            languages=[Lang("de")],
            url="brand.de.localhost",
            basic_auth=False
        ),
        BrandCountry(
            code="SE",
            languages=[Lang("sv")],
            url="brand.se.localhost",
            basic_auth=False
        ),
    ]
)

Brands = [BrandA, BrandB]