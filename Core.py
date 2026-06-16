cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_results = {}

print("\n" + "=" * 60)
print("  5-Fold Stratified Cross-Validation Results")
print("=" * 60)
