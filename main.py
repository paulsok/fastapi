from fastapi import FastAPI, Depends


app = FastAPI()

dummy_db = {
    '1': "SDE1 at Google",
    '2': "SDE2 at Amazon",
    '3': "Backend Dev. at Spotify",
    '4': "Senior Engineer at Alphabet",
    '5': "Devops Eng. at Microsoft",
}

class GetObjectOrFeatured:
    """We let companies promote their jobs. The promoted job
    is called featured_job"""

    def __init__(self, featured_job: str):
        self.featured_job = featured_job

    def __call__(self, id: str) -> str:
        value = dummy_db.get(id)
        if not value:
            value = dummy_db.get(self.featured_job)
        return value


@app.get("/job/{id}")
def get_job_by_id(job_title: str = Depends(GetObjectOrFeatured('2'))):
    return job_title
