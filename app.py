import streamlit as st
import datetime
import os
from pathlib import Path

def main():
    st.title("Pricing Model Run Settings")
    
    # Sidebar for configuration
    st.sidebar.header("Configuration Settings")
    
    # Valuation date picker
    val_date = st.date_input(
        "Valuation Date",
        value=datetime.date.today(),
        help="Select the valuation date for the pricing model"
    )
    
    
    # File uploader for assumption table
    assumption_file = st.file_uploader(
        "Choose Assumption Table",
        type=["xlsx", "csv"],
        help="Upload the assumption table file (Excel or CSV)"
    )

    # File uploader for data files
    data_file = st.file_uploader(
        "Choose Data Files",
        type=["xlsx", "csv"],
        help="Upload the data files (Excel or CSV)"
    )
    
    # Projection period slider
    projection_period = st.slider(
        "Projection Period (Years)",
        min_value=1,
        max_value=50,
        value=20,
        help="Select the projection period in years"
    )
    
    # Product group multiselect
    product_groups = [
        "Term Life",
        "Whole Life",
        "Universal Life",
        "Variable Life",
        "Annuities",
        "Group Insurance"
    ]
    
    selected_products = st.multiselect(
        "Select Product Groups to Run",
        options=product_groups,
        default=["Term Life"],
        help="Choose one or more product groups to include in the run"
    )
    
    # Run button with summary
    if st.button("Run Pricing Model"):
        if validate_inputs(val_date, assumption_file, data_file, selected_products):
            st.success("Run settings validated! Summary of settings:")
            display_summary(val_date, assumption_file, data_file, 
                          projection_period, selected_products)
            # Here you would add the actual call to your pricing model
            run_pricing_model(val_date, assumption_file, data_file, 
                            projection_period, selected_products)
        else:
            st.error("Please fill in all required fields")

def validate_inputs(val_date, assumption_file, data_file, selected_products):
    """Validate that all required inputs are provided"""
    if not val_date:
        return False
    if assumption_file is None:
        return False
    if data_file is None:
        return False
    if not selected_products:
        return False
    return True

def display_summary(val_date, assumption_file, data_file, 
                   projection_period, selected_products):
    """Display a summary of the run settings"""
    st.write("---")
    st.write("### Run Settings Summary")
    st.write(f"**Valuation Date:** {val_date}")
    st.write(f"**Assumption Table:** {assumption_file.name if assumption_file else ''}")
    st.write(f"**Data File:** {data_file.name if data_file else ''}")
    st.write(f"**Projection Period:** {projection_period} years")
    st.write("**Selected Products:**")
    for product in selected_products:
        st.write(f"- {product}")

def run_pricing_model(val_date, assumption_file, data_file, 
                     projection_period, selected_products):
    """
    Placeholder for the actual pricing model execution
    You would implement your model calling logic here
    """
    st.write("---")
    st.write("### Running Pricing Model")
    st.write("Processing...")
    # Add your model execution code here
    
if __name__ == "__main__":
    main() 