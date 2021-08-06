import style from "./style.css";
import axios from 'axios';

function Header(props){
	const apiurl = "http://localhost:5000/api/goods";
	async function search(event){
		event.preventDefault();
		var asset_id=document.getElementById("asset_id").value;
		var config = {
			method: 'POST',
			url: `${apiurl}/search`,
			headers: { 
				'Content-Type': 'application/json'
			},
			data : {
				"asset_id":asset_id
			}
		};
		axios(config)
		.then(function (response) {
				console.log(response.data);
		})
		.catch(function (error) {
			alert("エラーが発生しました。");
		});
	}
	return (
		<nav class={style.navbar} role="navigation" aria-label="main navigation">
			<div class="is-flex is-justify-content-space-between is-align-items-center">
				<div class="navbar-brand">
					<a class="navbar-item" href="/">
						<h1 class="is-size-3">3eets</h1>
					</a>
				</div>
				<div class="is-flex">
					
					<div class="buttons navbar-item are-small">
						<a href="/auth/login" class=" button is-primary">
							<strong>出品</strong>
						</a>
						<a href="/auth/login" class="button is-primary">
							<strong>ログイン</strong>
						</a>
					</div>
				</div>
			</div>
			<form onSubmit={search}>
				<div class="control navbar-item">
					<input class="input" type="text" name="asset_id" id="asset_id" placeholder="グッズを検索できます。" required/>
					<button type="submit"></button>
				</div>
			</form>
		</nav>
	)
}


export default Header;
