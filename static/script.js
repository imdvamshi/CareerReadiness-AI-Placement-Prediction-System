async function Prediction(){
    const data={
        age : parseInt(document.getElementById('age').value),
        gender : document.getElementById('gender').value,
        cgpa : parseFloat(document.getElementById('cgpa').value),
        branch : document.getElementById('branch').value,
        tier : document.getElementById('college-tier').value,
        internships : parseInt(document.getElementById('internships').value),
        projects : parseInt(document.getElementById('projects').value),
        certifications : parseInt(document.getElementById('certifications').value),
        coding : parseFloat(document.getElementById('coding').value),
        aptitude : parseFloat(document.getElementById('aptitude').value),
        communication : parseFloat(document.getElementById('communication').value),
        logical : parseFloat(document.getElementById('logical').value),
        hackathons : parseInt(document.getElementById('hackathons').value),
        github : parseInt(document.getElementById('github').value),
        linkedin : parseInt(document.getElementById('linkedin').value),
        mock : parseFloat(document.getElementById('mockinterview').value),
        attendance : parseFloat(document.getElementById('attendance').value),
        backlogs : parseInt(document.getElementById('backlogs').value),
        extra : parseFloat(document.getElementById('extra').value),
        leadership : parseFloat(document.getElementById('leadership').value),
        volunteer : document.getElementById('volunteer').value,
        sleep : parseInt(document.getElementById('sleep').value),
        study : parseInt(document.getElementById('study').value),
    };
    const response = await fetch("/predict",{
        method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(data)
    });
    const result = await response.json();
    document.getElementById('result').innerHTML = result.prediction;
}