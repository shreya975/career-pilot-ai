export default function ProjectsList({ roadmap }) {

  const projectPhase = roadmap.phases.find(
    (p) => p.projects
  );

  if (!projectPhase) return null;

  return (
    <div className="card">

      <h2>Projects</h2>

      {projectPhase.projects.map((project, i) => (
        <p key={i}>{project}</p>
      ))}

    </div>
  );
}
