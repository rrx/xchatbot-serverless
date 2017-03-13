import os
__here__ = os.path.dirname(os.path.realpath(__file__))
import logging
log = logging.getLogger(__name__)


def setup_nltk_on_lambda():
    """
    Getting nltk to run on lambda is tricky.

    We need to pregenerate the nltk libraries we are going to use
    and make them available to lambda
    """
    # we have to force the home variable in order to download
    # nltk files to the correct place for packaging
    os.environ['HOME'] = __here__
    from nltk.downloader import Downloader
    import nltk

    # deployed version of nltk data
    nltk.data.path = [os.path.join(__here__, 'nltk_data')] + nltk.data.path

    log.info("NLTK Path: %s", nltk.data.path)
    log.info("Default NLTK dir: %s", Downloader().default_download_dir())

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
