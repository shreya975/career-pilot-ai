export default function AnalyzeButton({ handleAnalyze, loading }) {
  return (
    <button onClick={handleAnalyze}>
      {loading ? "Analyzing..." : "Analyze"}
    </button>
  );
}
