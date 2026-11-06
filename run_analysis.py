from pathlib import Path

import duckdb


def run_sql_analysis():
    """Execute all MarketIQ SQL analyses and export results."""

    sql_folder = Path("sql")
    output_folder = Path("data/processed")
    output_folder.mkdir(parents=True, exist_ok=True)

    connection = duckdb.connect()

    for sql_file in sorted(sql_folder.glob("*.sql")):

        query = sql_file.read_text(encoding="utf-8")
        result = connection.execute(query).df()

        output_file = output_folder / f"{sql_file.stem}.csv"
        result.to_csv(output_file, index=False)

        print(
            f"SUCCESS: {sql_file.name} "
            f"-> {output_file}"
        )

    connection.close()

    print("\nAll SQL analyses completed successfully!")


if __name__ == "__main__":
    run_sql_analysis()