/* ===========================
   LOCALIZATION
=========================== */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const form =
            document.getElementById(
                "localizationForm"
            );

        if(form){

            form.addEventListener(

                "submit",

                async (e)=>{

                    e.preventDefault();

                    const fd =
                        new FormData(form);

                    const response =
                        await fetch(
                            "/localize",
                            {
                                method:"POST",
                                body:fd
                            }
                        );

                    const data =
                        await response.json();

                    document
                        .getElementById(
                            "localizationResult"
                        )
                        .textContent =

                        JSON.stringify(
                            data,
                            null,
                            2
                        );

                }

            );

        }

        loadTrajectory();

        loadAnalytics();

        loadKeyframes();

    }
);

/* ===========================
   TRAJECTORY
=========================== */

async function loadTrajectory(){

    const div =
        document.getElementById(
            "trajectoryPlot"
        );

    if(!div) return;

    const response =
        await fetch(
            "/trajectory/data"
        );

    const data =
        await response.json();

    const x =
        data.map(
            d => d.x
        );

    const y =
        data.map(
            d => d.y
        );

    const trace = {

        x:x,

        y:y,

        mode:"lines",

        type:"scatter"
    };

    Plotly.newPlot(

        "trajectoryPlot",

        [trace],

        {
            title:
            "Mission Trajectory"
        }

    );

}

/* ===========================
   ANALYTICS
=========================== */

async function loadAnalytics(){

    const roll =
        document.getElementById(
            "rollChart"
        );

    if(!roll) return;

    const response =
        await fetch(
            "/analytics/sensors"
        );

    const data =
        await response.json();

    const t =
        data.map(
            d => d.timestamp_ns
        );

    createChart(
        "rollChart",
        t,
        data.map(d=>d.roll),
        "Roll"
    );

    createChart(
        "pitchChart",
        t,
        data.map(d=>d.pitch),
        "Pitch"
    );

    createChart(
        "yawChart",
        t,
        data.map(d=>d.yaw),
        "Yaw"
    );

    createChart(
        "distanceChart",
        t,
        data.map(d=>d.distance_m),
        "Distance"
    );

}

function createChart(
    div,
    x,
    y,
    title
){

    Plotly.newPlot(

        div,

        [
            {
                x:x,
                y:y,
                type:"scatter"
            }
        ],

        {
            title:title
        }

    );

}

/* ===========================
   KEYFRAMES
=========================== */

async function loadKeyframes(){

    const div =
        document.getElementById(
            "keyframes"
        );

    if(!div) return;

    const response =
        await fetch(
            "/slam/keyframes"
        );

    const data =
        await response.json();

    div.textContent =

        JSON.stringify(
            data,
            null,
            2
        );
}