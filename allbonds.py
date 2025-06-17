import os
from datetime import date as dateType
from pathlib import Path
from typing import Optional
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()


CSV_FILE_PATH = Path(__file__).parent / "allbonds.csv"


class AllBondsData(BaseModel):
    """Response model for the all bonds data."""

    date: dateType = Field(
        description="Date of the data point, formatted as YYYY-MM-DD",
    )
    yc: str = Field(description="Yield Curve identifier", title="YC")
    y1: Optional[float] = Field(
	default=None,
        description="1 Year Yield",
        title="Y1Y",
        json_schema_extra={
            "x-widget_config": {
                "formatterFn": "percent",
            }
        },
    )
    y2: Optional[float] = Field(
	default=None,
        description="2 Year Yield",
        title="Y2Y",
        json_schema_extra={
            "x-widget_config": {
                "formatterFn": "percent",
            }
        },
    )
    y5: Optional[float] = Field(
	default=None,
        description="5 Year Yield",
        title="Y5Y",
        json_schema_extra={
            "x-widget_config": {
                "formatterFn": "percent",
            }
        },
    )
    y10: Optional[float] = Field(
	default=None,	
        description="10 Year Yield",
        title="Y10Y",
        json_schema_extra={
            "x-widget_config": {
                "formatterFn": "percent",
            }
        },
    )
    y30: Optional[float] = Field(
        default=None,
        description="30 Year Yield",
        title="Y30Y",
        json_schema_extra={
            "x-widget_config": {
                "formatterFn": "percent",
            }
        },
    )


def read_allbonds_csv() -> list:
    """
    Reads the allbonds.csv file and returns its content as a list of dictionaries.
    Each dictionary represents a row in the CSV, with column headers as keys.
    This function is called every time the API endpoint is accessed to ensure
    the latest data is always served.
    """
    if not os.path.exists(CSV_FILE_PATH):
        print(f"DEBUG: CSV file NOT found at {CSV_FILE_PATH} when trying to read.")
        return []
    try:
        df = pd.read_csv(CSV_FILE_PATH)

        # Check for empty DataFrame after reading, even if file existed
        if df.empty:
            print(f"DEBUG: CSV file '{CSV_FILE_PATH}' was read successfully but resulted in an empty DataFrame.")
            return []

        # Replace NaN values with None (JSON compliant 'null')
        df = df.replace({np.nan: None, np.inf: None})
        print(f"Successfully read {len(df)} rows from {CSV_FILE_PATH}")
        # Convert DataFrame to a list of dictionaries (records format)
        return df.to_dict(orient="records")

    except Exception as e:
        print(f"ERROR: Exception while reading or processing CSV file: {e}")
        return []


@app.get("/get_all_bonds", response_model=list[AllBondsData])
async def get_all_bonds_data():
    """Fetch all data from the allbonds.csv file."""
    try:
        return read_allbonds_csv()
    except Exception:
        return JSONResponse(content={"message": "Could not load data from allbonds.csv"}, status_code=500)