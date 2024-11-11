from fastapi import FastAPI
from . import (
    CheckSeasonLog,
    FetchLatestSynchronousData,
    LoadUserDataAll,
    UpdateFormation,
    ChangeCurrentAnnouncer,
    SetPersonalityGacksungIllust,
    GetUserCouponState,
    # UseCoupon,
)


def add_api_handler(app: FastAPI):
    app.post("/api/FetchLatestSynchronousData")(FetchLatestSynchronousData.handle)
    app.post("/api/LoadUserDataAll")(LoadUserDataAll.handle)
    app.post("/api/CheckSeasonLog")(CheckSeasonLog.handle)
    app.post("/api/UpdateFormation")(UpdateFormation.handle)
    app.post("/api/ChangeCurrentAnnouncer")(ChangeCurrentAnnouncer.handle)
    app.post("/api/SetPersonalityGacksungIllust")(SetPersonalityGacksungIllust.handle)
    app.post("/api/GetUserCouponState")(GetUserCouponState.handle)
    # app.post("/api/UseCoupon")(UseCoupon.handle)
