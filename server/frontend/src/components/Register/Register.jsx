import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png"
import email_icon from "../assets/email.png"
import password_icon from "../assets/password.png"
import close_icon from "../assets/close.png"

const Register = () => {

    const [firstName, setFirstName] = useState("");
    const [lastName, setlastName] = useState("");
    const [email, setEmail] = useState("");
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");


    const gohome = ()=> {
        window.location.href = window.location.origin;
    };

    const register = async (e) => {
        e.preventDefault();

        let register_url = window.location.origin+"/djangoapp/register";
        
        const res = await fetch(register_url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "userName": userName,
                "password": password,
            }),
        });

        const json = await res.json();

        if (json.status) {
            sessionStorage.setItem('username', json.userName);
            window.location.href = window.location.origin;
        } else if (json.error === "Already Registered") {
            alert("The user with same username is already registered");
            window.location.href = window.location.origin;
        };
    };

    return (
        <div className="register_container" style={{width: "50%"}}>

            {/* Header */}
            <div className="header" style={{display: "flex",flexDirection: "row", justifyContent: "space-between"}}>
                <span className="text" style={{flexGrow:"1"}}>SignUp</span>

                {/* Close button, "x" */}
                <div style={{display: "flex",flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
                    <a href="/" onClick={()=>{gohome()}} style={{justifyContent: "space-between", alignItems:"flex-end"}}>
                        <img style={{width:"1cm"}} src={close_icon} alt="X"/>
                    </a>
                </div>

                <hr/>

            </div>

            {/* Form */}
            <form onSubmit={register}>

                {/* Inputs Panel */}
                <div className="inputs">

                    {/* First Name */}
                    <div>
                        <img src={user_icon} className="img_icon" alt='First Name'/>
                        <input type="text"  name="first_name" placeholder="First Name" className="input_field" onChange={(e) => setFirstName(e.target.value)}/>
                    </div>

                    {/* Last Name */}
                    <div>
                        <img src={user_icon} className="img_icon" alt='Last Name'/>
                        <input type="text"  name="last_name" placeholder="Last Name" className="input_field" onChange={(e) => setlastName(e.target.value)}/>
                    </div>

                    {/* Email */}
                    <div>
                        <img src={email_icon} className="img_icon" alt='Email'/>
                        <input type="email"  name="email" placeholder="email" className="input_field" onChange={(e) => setEmail(e.target.value)}/>
                    </div>

                    {/* Username */}
                    <div className="input">
                        <img src={user_icon} className="img_icon" alt='Username'/>
                        <input type="text"  name="username" placeholder="Username" className="input_field" onChange={(e) => setUserName(e.target.value)}/>
                    </div>

                    {/* Password */}
                    <div className="input">
                        <img src={password_icon} className="img_icon" alt='password'/>
                        <input name="psw" type="password"  placeholder="Password" className="input_field" onChange={(e) => setPassword(e.target.value)}/>
                    </div>

                </div>

                {/* Submission Panel */}
                <div className="submit_panel">
                    <input className="submit" type="submit" value="Register"/>
                </div>
            </form>

        </div>
    );
};

export default Register;
