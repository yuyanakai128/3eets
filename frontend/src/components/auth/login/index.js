import style from	"./style.css";
import LoginHeader from "../header/login_header"
import {login} from "../../../assets/js/login"



const Login = () => {

    async function handleLogin(event){
        event.preventDefault();
        var email =  document.getElementById('email').value;
        var password = document.getElementById("password").value;
		
        await login(email, password);
    }
	return (
		<>
		<LoginHeader/>
		<div class="field" class={style.login}>
			<form onSubmit={handleLogin}>
				<div class="field mb-5">
					<label class="is-size-6"><strong>メールアドレス</strong></label>
					<div class="control">
						<input class="input" type="email" name="email" id="email" placeholder="" required/>
					</div>
				</div>
				<div class="field">
					<label class="is-size-6"><strong>パスワード</strong></label>
					<div class="control">
						<input class="input" type="password" name="password" id="password" placeholder="" required/>
					</div>
				</div>
				<div class="field mt-6">
					<div clas="control ">
						<button type="submit" class="button is-primary is-fullwidth" ><strong>ログイン</strong></button>
					</div>
				</div>
				<div class="field has-text-centered is-size-7 my-5">
					<a href="/auth/password"><strong>パスワードを忘れた方はこちら</strong></a>
				</div>
			</form>
			
			<div class="field has-text-centered is-size-6 my-5">
				<label class="is-size-6"><strong>アカウントをお持ちでない方は</strong></label>
			</div>
			<div class="field mt-5">
				<div clas="control ">
					<a href="/auth/register" class="button is-primary is-fullwidth is-outlined" ><strong>新規会員登録</strong></a>
				</div>
			</div>
		</div>
		</>
	);
}

export default Login;
