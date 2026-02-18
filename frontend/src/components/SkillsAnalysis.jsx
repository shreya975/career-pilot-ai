export default function SkillsAnalysis({ skills }) {

  if (!skills) return null;

  return (

    <div className="bg-card p-6 rounded-xl shadow">

      <h2 className="text-lg font-semibold mb-4">
        Skills
      </h2>

      <div className="flex flex-wrap gap-2">

        {skills.detected.map((skill, i) => (

          <span
            key={i}
            className="bg-primary px-3 py-1 rounded-full text-sm"
          >
            {skill}
          </span>

        ))}

      </div>

    </div>

  );

}
