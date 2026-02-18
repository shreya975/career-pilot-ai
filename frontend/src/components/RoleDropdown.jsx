export default function RoleDropdown({ role, setRole }) {
  return (
    <div>
      <h3>Select Role</h3>

      <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="">Auto Detect</option>
        <option>Backend Developer</option>
        <option>Frontend Developer</option>
        <option>Full Stack Developer</option>
        <option>AI Engineer</option>
      </select>

    </div>
  );
}
