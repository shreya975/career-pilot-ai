export default function SkillsInput({ skills, setSkills }) {
  return (
    <div>
      <h3>Enter Skills</h3>
      <input
        type="text"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
        placeholder="python, react, docker"
      />
    </div>
  );
}
