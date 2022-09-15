from datasets import list_datasets

# build a dataset search query
def search(query, limit=10, sort=True):
    """Search for a dataset by name or description"""

    # get all datasets that match the query
    datasets = [dataset for dataset in list_datasets() if query in dataset]
    sorted_datasets = sorted(datasets) if sort else datasets
    limited_result = sorted_datasets if limit is None else sorted_datasets[:limit]
    return limited_result


# Load a dataset and print the first example in the training set
# squad_dataset = load_dataset('squad')
# print(squad_dataset['train'][0])
