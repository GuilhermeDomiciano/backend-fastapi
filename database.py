from sqlmodel import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres.khaajlvbbipyotipikew:encoinfominicurso2025@aws-1-sa-east-1.pooler.supabase.com:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=5,
    max_overflow=10,
    connect_args={
        "sslmode": "require"
    }
)                                       