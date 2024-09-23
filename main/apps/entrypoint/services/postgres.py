from django.shortcuts import get_object_or_404

def create(write_serializer, read_serializer, data_dict):
    serializer = write_serializer(data=data_dict)
    if serializer.is_valid():
        model_instance = serializer.save()
        metadata_dict = read_serializer(model_instance).data
        return metadata_dict

def retrieve(model, read_serializer, api_key_str):
    api_key_dict = {'key': api_key_str}
    model_instance = get_object_or_404(model, **api_key_dict)
    serializer = read_serializer(model_instance)
    metadata_dict = serializer.data
    return metadata_dict
