from django.shortcuts import render
from .model_loader import predict_from_dict, _feature_names

def homepage(request):
    return render(request, "predictor/home.html")

def predict_page(request):
    result = None
    if request.method == "POST":
        input_data = {}
        for f in _feature_names:
            val = request.POST.get(f)
            try:
                # Convert to appropriate type based on field name
                if f == "Gender":
                    input_data[f] = int(val)  # Convert to integer for Gender
                else:
                    input_data[f] = float(val)  # Convert to float for numeric fields
            except (ValueError, TypeError):
                # Set default values if conversion fails
                if f == "Gender":
                    input_data[f] = 1  # Default to Male (1)
                else:
                    input_data[f] = 0.0  # Default to 0.0 for numeric fields
        
        result = predict_from_dict(input_data)
    
    return render(request, "predictor/predict.html", {
        "feature_names": _feature_names, 
        "result": result
    })
    
    # #sample_patient = [45, 1, 1.2, 0.5, 200, 30, 40, 4.5, 1.2]