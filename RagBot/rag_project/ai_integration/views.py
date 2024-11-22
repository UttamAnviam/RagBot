
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def ask_database(request):

    file_path = "ai_integration\\transcriptions.csv"

    loader = CSVLoader(file_path=file_path)
    data = loader.load()

    # Load example document
   

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=2000,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.split_text(data)
    print(texts[0])
    print(texts[1])


# def home_view(request):
#     return render(request, 'index.html')