import style from	"./style.css";
import Header from "../header"
import {register} from "../../../assets/js/login"

const Register = () => {
	async function handleRegister(event){
        event.preventDefault();
        var name =  document.getElementById('name').value;
		var email = document.getElementById('email').value;
        var password = document.getElementById("password").value;
		var password_r = document.getElementById("password_r").value;
		
        await register(name, email, password);
    }
	return (
		<div>
			<Header />
			<form onSubmit={handleRegister} class="field" class={style.login}>
				<div>
					<div class="field mb-5">
						<label class="is-size-6"><strong>名前</strong></label>
						<div class="control">
							<input class="input" name="name" id="name" type="text" placeholder="" required/>
						</div>
					</div>
					<div class="field mb-5">
						<label class="is-size-6"><strong>Email</strong></label>
						<div class="control">
							<input class="input" name="email" id="email" type="email" placeholder="" required/>
						</div>
					</div>
					<div class="field mb-5">
						<label class="is-size-6"><strong>パスワード</strong></label>
						<div class="control">
							<input class="input" name="password" id="password" type="password" placeholder="" required/>
						</div>
					</div>
					<div class="field mb-5">
						<label class="is-size-6"><strong>パスワード</strong></label>
						<div class="control">
							<input class="input" name="password_r" id="password_r" type="password" placeholder="" required/>
						</div>
					</div>
				</div>

				<div class="field mt-6">
					<div clas="control ">
						<button type="submit" class="button is-primary is-fullwidth" href="/auth/login" ><strong>新規会員登録</strong></button>
					</div>
				</div>
			</form>
		</div>
	);
}

export default Register;
