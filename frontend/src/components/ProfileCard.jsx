export default function ProfileCard({ profile }) {

  if (!profile) return null;

  return (

    <div className="bg-card p-6 rounded-xl shadow">

      <h2 className="text-lg font-semibold mb-4">
        Profile Summary
      </h2>

      <p>
        Best Role:
        <span className="text-primary ml-2">
          {profile.best_role}
        </span>
      </p>

      <p>
        Resume Score:
        <span className="ml-2">
          {profile.resume_score}%
        </span>
      </p>

      <p>
        Match Score:
        <span className="ml-2">
          {profile.match_score}%
        </span>
      </p>

    </div>

  );

}
