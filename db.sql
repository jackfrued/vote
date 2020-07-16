drop database if exists `vote`;

create database `vote` default charset utf8;

use `vote`;

-- 创建学科表
create table `tb_subject` (
	`no` integer not null auto_increment comment '编号',
	`name` varchar(50) not null comment '名称',
	`intro` varchar(1000) not null default '' comment '介绍',
	`is_hot` boolean not null default 0 comment '是否热门',
	primary key (`no`)
);

-- 创建老师表
create table `tb_teacher` (
	`no` integer not null auto_increment comment '编号',
	`name` varchar(20) not null comment '姓名',
	`sex` boolean not null default 1 comment '性别',
	`birth` date not null comment '出生日期',
	`intro` varchar(1000) not null default '' comment '介绍',
	`photo` varchar(255) not null default 'default.png' comment '照片',
	`gcount` integer not null default 0 comment '好评数',
	`bcount` integer not null default 0 comment '差评数',
	`sno` integer not null comment '所属学科',
	primary key (`no`),
	foreign key (`sno`) references `tb_subject` (`no`)
);

-- 插入学科记录
insert into `tb_subject`
	(`name`, `intro`, `is_hot`)
values
	('Python全栈+人工智能', 'Python是一门简单、优雅、高效的编程语言，国内外诸多互联网企业都在使用Python语言并将其应用于后端开发、数据采集、数据分析、量化交易、自动化运维、自动测试等领域，从国内的华为、阿里、腾讯、美团到国外的Facebook、LinkedIn、Amazon、Google，很多互联网企业都有自己的Python研发团队。近年来随着大数据和人工智能产业的崛起以及企业对数据驱动决策的需求，数据分析和人工智能等领域出现了巨大的Python人才缺口，企业对Python开发者的需求更是以每年150%的趋势增长。国内一线城市，Python开发者平均月薪高达20000元以上，数据分析和人工智能的从业者月薪更是远高于行业平均水平。', 1),
	('全链路UI/UE设计', '以行业潮流设计为导向设计课程，抛弃传统的培训模式，采用以全链路的形式培养行业急需的复合型设计人才，让学员学会将设计的价值融入每一个和用户的接触点中，让整个业务的用户体验质量得到几何级数的增长，并培养学员具备整合、统筹整个设计环节的能力。全链路UI/UE坚持紧跟行业急需设计升级课程，保证满足行业的需求。同时采用学科联合的模式开发真实上线项目，让学员感受企业项目开发过程、团队配合、项目提案及路演全过程，让学员从思想上转变为设计师身份，提高学习和动手能力，毕业快速适应企业的工作节奏与项目分工。', 0),
	('JavaEE+分布式开发', 'Java语言历经20余年的雕琢，已经涵盖到软件开发的各个领域。从桌面应用到Web应用，从个人手持设备到大型服务器集群，IT行业中随处可见Java的身影；从小规模的单体应用到中等规模的集群应用再到千万级访问的高并发应用，Java生态圈都能给出完美的解决方案。作为编程领域的王者，Java语言拥有全球最大的开发者群体和最强的技术生态圈；作为后端开发的首选语言，Java语言为企业孕育了一批又一批程序员和架构师，引领着整个软件行业的发展。', 0),
	('HTML5大前端', '随着互联网和移动互联网的飞速发展，形形色色的网站和五花八门的App层出不穷；为了打造更好的互联网产品，游戏、社交、电商、金融、教育等行业对前端开发者的需求更是达到了前所未有的高度。HTML5作为万维网的核心和前端开发的基石, 凭借着跨平台、低成本、快速迭代、高效分发等优势，迅速成为了互联网产品研发的关键技术。近年来，从PC端开发到移动端开发再到小程序开发，前端开发的相关技术和工具一直处于持续发展状态；从初创企业到上市公司再到行业巨头，对前端开发者的人才需求一直保持巨大缺口，优秀的Web前端工程师仍然是“一将难求”。', 1);

-- 插入老师记录
insert into `tb_teacher`
	(`name`, `sex`, `birth`, `intro`, `photo`, `sno`)
values
	('骆昊', 1, '1980-11-28', '15年以上产品设计和研发经验，工学博士，参与过3项国家自然科学基金项目和多项科技攻关项目的研发，发表过1篇SCI和3篇EI论文。分布式网络性能测量系统的设计者，perf-TTCN3语言的发明者。CSDN博客专家，GitHub网站8w+星标项目Python-100-Days作者。精通C/C++、Java、Python、SQL等编程语言，擅长OOAD、系统架构、算法设计、数据分析，一直践行“用知识创造快乐”的教学理念，善于总结，乐于分享。', 'luohao.png', 1),
	('余婷', 0, '1992-4-9', '5年以上移动互联网项目开发经验和教学经验，曾担任上市游戏公司高级软件研发工程师和技术负责人，参与多个游戏类应用移动端和后台程序研发，拥有丰富的项目开发和管理经验，在苹果的AppStore上发布过多款应用。精通Python、Objective-C、Swift等开发语言，熟悉移动App和RESTful接口开发相关技术。授课条理清晰、细致入微，有较强的亲和力，教学过程注重理论和实践的结合，在学员中有良好的口碑。', 'yuting.png', 1),
	('张无忌', 1, '1988-7-6', '中土明教第三十四代教主。武当七侠之一张翠山与天鹰教紫微堂主殷素素之子，明教四大护教法王之一金毛狮王谢逊义子。出生起在冰火岛过着原始生活，踏足中土后即幼失怙恃，中玄冥神掌寒毒命危，后在蝴蝶谷带病习医，义送孤儿至西域，在昆仑仙谷绝处逢生。忍受寒毒煎熬七年，福缘际会，融合九阳神功、乾坤大挪移、太极拳（及太极剑）和圣火令神功四大盖世武功为一体，当世无敌。此外还精研医术和毒术，术绝尘寰。', 'zhangwuji.png', 2),
	('韦一笑', 1, '1979-12-5', '在明教四大护教法王“紫白金青”中排行最末，因其轻功绝顶，又吸食鲜血，故绰号“青翼蝠王”。与布袋和尚说不得是生死之交。其轻功可谓无与伦比，当世无双，这种绝世轻功不是练出来的，而是天赋异禀可以说是天赐，在修炼“寒冰绵掌”时出了差错，经脉中郁积了寒毒，一用内力寒毒就会发作，要吸人血免去全身血脉凝结成冰。后得到张无忌“九阳神功”治疗祛除了寒毒摆脱嗜血的命运。', 'weiyixiao.png', 4);

-- 插入用户记录
-- insert into `tb_user`
--     (`username`, `password`, `tel`, `reg_date`)
-- values
--     ('wangdachui', '1c63129ae9db9c60c3e8aa94d3e00495', '13122334455', now()),
--     ('hellokitty', 'c6f8cf68e5f68b0aa4680e089ee4742c', '13890006789', now());
