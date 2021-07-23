import style from	"./style.css";
import Header from "../header"
import {getUserData} from "../../../assets/js/login"



const Password = () => {

    async function PasswordBack(event){
        event.preventDefault();
        var email =  document.getElementById('email').value;
		
        await getUserData(email);
    }
	return (
		<>
		<Header/>
		<div class="field" class={style.login}>
			<form onSubmit={PasswordBack}>

				<div class="field">
					<label class="is-size-6"><strong>Email</strong></label>
					<div class="control">
						<input class="input" type="email" name="email" id="email" placeholder="" required/>
					</div>
				</div>
				<div class="field mt-6">
					<div clas="control ">
						<button type="submit" class="button is-primary is-fullwidth" ><strong>Send</strong></button>
					</div>
				</div>
				<div class="field has-text-centered is-size-7 my-5">
					{/* <strong>パスワードを忘れた方はこちら</strong>	 */}
				</div>
			</form>
		</div>
		</>
	);
}

export default Password;
