import style from "./style.css";
import Header from "../header";
import Common from "../../common";
import CommonButton from "../../commonButton";
import Footer from "../../footer";

function Dashborad(props){
	
	return  (
	<>
		<Header />
		<Common />
		<CommonButton />
		<div class="is-flex is-flex-wrap-wrap p-3">
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img2.png"/>
				<p class={style.text1}>指定なし</p>
				<p class={style.text2}>指定なし</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img4.png"/>
				<p class={style.text1}>同種</p>
				<p class={style.text2}>手渡し</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img3.png"/>
				<p class={style.text1}>異種</p>
				<p class={style.text2}>郵送</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>

		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img2.png"/>
				<p class={style.text1}>指定なし</p>
				<p class={style.text2}>指定なし</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img4.png"/>
				<p class={style.text1}>同種</p>
				<p class={style.text2}>手渡し</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img3.png"/>
				<p class={style.text1}>異種</p>
				<p class={style.text2}>郵送</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>

		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img2.png"/>
				<p class={style.text1}>指定なし</p>
				<p class={style.text2}>指定なし</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img4.png"/>
				<p class={style.text1}>同種</p>
				<p class={style.text2}>手渡し</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img3.png"/>
				<p class={style.text1}>異種</p>
				<p class={style.text2}>郵送</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>

		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img2.png"/>
				<p class={style.text1}>指定なし</p>
				<p class={style.text2}>指定なし</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img4.png"/>
				<p class={style.text1}>同種</p>
				<p class={style.text2}>手渡し</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
		<div class="good-container mx-2">
			<div class={style.goodsimage}>
				<img class={style.goodsImg} src="../assets/image/img3.png"/>
				<p class={style.text1}>異種</p>
				<p class={style.text2}>郵送</p>
			</div>
			<p class="is-size-7">グッズ名グッズ…</p>
			<p>¥25,555</p>
		</div>
	</div>
		<Footer />
		</>
		)
}


export default Dashborad;