import os
import pdfplumber
import pandas as pd

class InputConverter:
    def convert(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[-1].lower()
        if ext == ".csv":
            return self._convert_csv(file_path)
        elif ext == ".pdf":
            return self._convert_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    def _convert_csv(self, file_path: str) -> str:
        df = pd.read_csv(file_path)
        return df.to_markdown(index=False)

    def _convert_pdf(self, file_path: str) -> str:
        def _dedup_columns(columns):
            """Ensure unique column names by appending suffix if needed."""
            seen = {}
            new_cols = []
            for col in columns:
                if col in seen:
                    seen[col] += 1
                    new_cols.append(f"{col}_{seen[col]}")
                else:
                    seen[col] = 0
                    new_cols.append(col)
            return new_cols

        all_tables = []
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                table = page.extract_table()
                if table:
                    df = pd.DataFrame(table[1:], columns=_dedup_columns(table[0]))
                    df["__page__"] = page_num  # keep track of page number
                    all_tables.append(df)

        if not all_tables:
            raise ValueError("No tables found in PDF.")

        # Format all tables separately into Markdown
        combined_markdown = ""
        for i, df in enumerate(all_tables, start=1):
            combined_markdown += f"\n### Table {i} (Page {df['__page__'].iloc[0]})\n"
            combined_markdown += df.drop(columns="__page__").to_markdown(index=False)
            combined_markdown += "\n"

        return combined_markdown