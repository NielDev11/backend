from fastapi import FastAPI
from routes.rmodulo import router as modulo_router
from routes.ratributo import router as atributo_router
from routes.rfacultad import router as facultad_router
from routes.rtipoevaluacion import router as tipoevaluacion_router
from routes.rperfil import router as perfil_router
from routes.rprograma import router as programa_router
from routes.rmoduloxperfil import router as moduloxperfil_router
from routes.rasignatura import router as asignatura_router
from routes.rgrupo import router as grupo_router
from routes.rusuario import router as usuario_router
from routes.revaluaciondoc import router as evaluaciondoc_router
from routes.reva_doc_asig_est import router as eva_doc_asig_est_router
from routes.rdetalleevadmon import router as detalleevadmon_router
from routes.rnivel import router as nivel_router
from routes.rcargo import router as cargo_router
from routes.rcompetencia import router as competencia_router
from routes.rcomportamiento import router as comportamiento_router
from routes.rbancopregunta import router as bancopregunta_router
from routes.revaluacionadmon import router as evaluacionadmon_router
from routes.rdetalleevadoc import router as detalleevadoc_router
from routes.rdetalle_evadoc_director import router as detalle_evadoc_director_router
from routes.reva_doc_director import router as eva_doc_director_router

from routes.ruser import router as user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    #"http://localhost"
    #"http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(modulo_router)
app.include_router(atributo_router)
app.include_router(facultad_router)
app.include_router(tipoevaluacion_router)
app.include_router(perfil_router)
app.include_router(programa_router)
app.include_router(moduloxperfil_router)
app.include_router(asignatura_router)
app.include_router(grupo_router)
app.include_router(usuario_router)
app.include_router(evaluaciondoc_router)
app.include_router(eva_doc_asig_est_router)
app.include_router(eva_doc_asig_est_router)
app.include_router(detalleevadmon_router)
app.include_router(nivel_router)
app.include_router(cargo_router)
app.include_router(competencia_router)
app.include_router(comportamiento_router)
app.include_router(bancopregunta_router)
app.include_router(evaluacionadmon_router)
app.include_router(detalleevadoc_router)
app.include_router(detalle_evadoc_director_router)
app.include_router(eva_doc_director_router)
app.include_router(user)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)