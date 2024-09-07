import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm

def process_excel(file):
    df = pd.read_excel(file, sheet_name='B2B')
    df = df.drop([0, 1, 2, 3, 4])
    df = df.infer_objects(copy=False)
    filters = [0, 0.25, 1.50, 3, 5, 12, 18, 28]

    results = []

    total_taxable_value = 0
    total_igst_value = 0
    total_cgst_value = 0
    total_sgst_value = 0

    for rate in filters:
        filtered_df = df[df['Unnamed: 8'] == rate]
        taxable_value = filtered_df['Unnamed: 9'].sum()
        igst_value = filtered_df['Unnamed: 10'].sum()
        cgst_value = filtered_df['Unnamed: 11'].sum()
        sgst_value = filtered_df['Unnamed: 12'].sum()

        total_taxable_value += taxable_value
        total_igst_value += igst_value
        total_cgst_value += cgst_value
        total_sgst_value += sgst_value

        results.append({
            "rate": rate,
            "taxable_value": taxable_value,
            "igst_value": igst_value,
            "cgst_value": cgst_value,
            "sgst_value": sgst_value
        })

    totals = {
        "total_taxable_value": total_taxable_value,
        "total_igst_value": total_igst_value,
        "total_cgst_value": total_cgst_value,
        "total_sgst_value": total_sgst_value,
    }

    return results, totals


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            results, totals = process_excel(file)

            return render(request, 'result.html', {
                'results': results,
                'totals': totals
            })
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
