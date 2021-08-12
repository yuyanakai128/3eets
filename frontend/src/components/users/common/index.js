import style from "./style.css";
import $ from "jquery";

const Common = (props) => {
  $('#'+style.toptab).on('click',function(){
    console.log($(this));
  })
	return (
    <>
      <div id={style.toptab}>
        <div id={style.exchange}  class={style.active}>
          <span>交換</span>
        </div>
        <div id={style.purchase}>
          <span>共同購入</span>
        </div>
      </div>
      <div id={style.ID3tab_dev}>
        <div id={style.recommendation}>
          <span>おすすめ</span>
        </div>
        <div id={style.mylist} class = {style.active}>
          <span>マイリスト</span>
        </div>
      </div>
    </>
  );
}

export default Common;
