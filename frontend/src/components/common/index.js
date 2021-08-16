import { useState } from 'preact/hooks';
import style from "./style.css";


const Common = (props) => {
  const [active, setActive] = useState(1);
  const [second, setSecond] = useState(1);
	return (
    <>
      <ul id={style.toptab}>
        <li id={style.exchange} class={active==1?style.active:""} onClick={()=>{setActive(1)}}>
          <span>交換</span>
        </li>
        <li id={style.purchase} class={active==2?style.active:""} onClick={()=>{setActive(2)}}>
          <span>共同購入</span>
        </li>
      </ul>
      <ul id={style.ID3tab_dev}>
        <li id={style.recommendation} class={second==1?style.active:""} onClick={()=>{setSecond(1)}}>
          <span>おすすめ</span>
        </li>
        <li id={style.mylist} class={second==2?style.active:""} onClick={()=>{setSecond(2)}}>
          <span>マイリスト</span>
        </li>
      </ul>
    </>
  );
}

export default Common;
