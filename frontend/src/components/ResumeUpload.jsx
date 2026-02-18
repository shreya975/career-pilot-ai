export default function ResumeUpload({ setFile }) {
  return (
    <div>
      <h3>Upload Resume</h3>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
    </div>
  );
}
