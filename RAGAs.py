import pandas as pd

df = pd.read_csv("")

print(f"Number of questions: {len(df)}")
print(f"\n{'='*40}")
print("Average Score：")
print(f"{'='*40}")

metrics = {
    "Faithfulness":                           "faithfulness",
    "Answer Relevancy":                       "answer_relevancy",
    "LLM Context Precision (w/o reference)":  "llm_context_precision_without_reference",
}

for name, col in metrics.items():
    mean = df[col].mean()
    nan  = df[col].isna().sum()
    print(f"  {name}: {mean:.4f}  (Fail: {nan})")

print(f"\n{'='*40}")
print("Score Distribution：")
print(f"{'='*40}")
for name, col in metrics.items():
    print(f"\n{name}:")
    print(f"  Max: {df[col].max():.4f}")
    print(f"  Min: {df[col].min():.4f}")
    print(f"  Median: {df[col].median():.4f}")



metrics = ["faithfulness", "answer_relevancy", "llm_context_precision_without_reference"]

failed = df[df[metrics].isna().any(axis=1)]

print(f"Fail: {failed.index.tolist()}")