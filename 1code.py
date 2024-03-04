if __name__ == "__main__":
    try:
        image_count = download_images_from_google_query(sys.argv[1])
        print(f"{image_count} images were downloaded to disk.")
    except IndexError:
        print("Please provide a search term.")
        raise

  class Parser(HTMLParser):
    def __init__(self, domain: str) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.domain = domain
def get_domain_name(url: str) -> str:
    """
    This function get the main domain name

    >>> get_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'c.d'
    >>> get_domain_name("Not a URL!")
    ''
    """
    return ".".join(get_sub_domain_name(url).split(".")[-2:])
