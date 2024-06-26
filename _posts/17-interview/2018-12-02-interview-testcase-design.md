---
layout: post
title: "基于脑图高效设计测试用例"
subtitle: '线上V咖分享'
author: "Haauleon"
header-style: text
tags:
  - 面试
---

&emsp;&emsp;首先要感谢刘琛梅老师分享了一篇名为【V咖分享会】测开第13期分享会为主题的公众号推文，才有了此次参加分享会和认识VIPTEST测开社群的机会，同时我也是刘老师《测试架构师修炼之道》的忠实读者。再来说说V社本期的线上社群V咖分享，本期V咖主讲人是李龙老师，著有《软件测试架构实践与精准测试》。很荣幸能够参加李龙老师的分享课，该篇博文目的意在把李龙老师在分享课上的语音记录转化为文字记录保存下来，留以分享。         
![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-1.jpg)




### 课堂内容

李龙老师：今天主要是和大家来探讨一下基于思维导图我们如何高效去设计测试用例的方法，还有一部分的案例分析。       

#### V社简介
李龙老师：刚才Mango介绍了一下VIPTEST社群的一些信息，正好我准备的资料里面也有部分文件可以先给大家截个图，也算是帮VIPTEST做一下宣传吧。           
![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-2.jpg)             

#### 主题目录    

李龙老师：今天我分享的主题就是如何基于思维导图高效设计测试用例的方法和案例分析，这个主题说实话它是比较老生常谈的话题，所有测试工程师都离不开做测试用例的设计的。可能这个主题所有人都敢讲也都敢说，但是有多少人真正的能把测试用例设计的非常高效，去平衡的标准是不一样的。然后VIPTest之前已经分享了12期了，之前的12期，每个人有讲大数据的、云计算的，还有一些自动化测试的，我讲的这个主题呢，还是回归到了根本，那就是最初的测试用例的设计，希望大家喜欢。       

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-3.jpg)      
李龙老师：今天我主要从五个方面给大家介绍。一个是和大家分析常规测试用例遇到的问题，后面就是引入脑图我们做软件测试的设计和分析，还有就是关于测试设计的一些要点和问题。       

李龙老师：我们所熟知的传统的测试用例设计编写起来，说实话编写起来说实话还是比较繁杂的。尤其是在大型的信息系统产品、快节奏的迭代项目和敏捷项目，甚至是耦合度高的产品中，传统的用例编写方法实际上很明显是滞后，或者是带来了较多冗余的工作量，它使我们测试的设计人员过度的关注于测试用例步骤的编写、修改，甚至是再修改，然后还要根据现有测试用例的设计原则保证唯一性和可追溯性，它会出现同一条测试用例经过多人执行永远得到相同的结果，这一点让人不得不想到另一个具有挑战性的词汇，那就是自动化测试。       

李龙老师：为什么要这样说呢？因为这种传统的用例设计的方式的话，他一次编写多人运行相同的结果，没有思考的过程，其实他是严重阻碍了测试执行人员或者是相关人员的创新意识的。并且加大了他们的工作量，其实还不如直接让自动化测试去取代。那么今天呢，我要给大家分享的是用思维导图的方式如何让不同的人，按照一定的思维方式设计出来的是测试用例或者所执行的测试用例，它的覆盖率会更高。因为这种方式，它可以很好的或者有效的杜绝一人编写，然后其他人没有思考，多人运行得到相同结果的一个用人工的方式来实现自动化的弊端。        

#### 测试用例设计的发展      

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-4.jpg)          
李龙老师：大家可以看一下我刚才贴的图片，这是经过多少年的一些积累。大部分的软件公司，他的软件测试用例的一些标准和模板。其实根据测试用例的定义以及他的六要素的一些内容，我们在经历了n多个项目之后，其实会发现工作起来精力也是越来越力不从心了。因为就像刚才说的，在现在软件行业的发展和快节奏下，任何一个测试项目都是需要经过高强度快速的一个迭代，而每次迭代设计编写的测试用例都包含了所有的测试要素，遇到项目有任何一些丁点儿的变更，测试步骤必须要重新的修改和完善。        

李龙老师：其实在这种高度紧张以及多人更改测试用例之后，我们就会感觉现在的测试用例越来越冗余，甚至有些鸡肋了。所以，我们不断的去有一些专家或者测试工程师一些高级的工程师，就去不断的突破创新，才引入了相关的基于脑图来进行测试用例的设计的这么一个概念。         

#### 常规测试用例遇到的问题     

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-5.jpg)
李龙老师：大家可以看一下，这是常规测试用例遇到的一些问题，比如说是测试用例里面写死了数据、业务步骤，因为不同的测试人员都会按照具体的操作步骤来进行测试。就好比我们在做车载导航测试一样，由于步骤的明确化，车载导航测试已经变成了导航测试。我不知道这句话大家能不能听明白，就是说我们要做的是他的车载的导航的能力，而不是我们预先制定了一个导航的一中模式，然后让所有的测试工程师按照具体的路径规划进行一个内容的验证，因为这样的话，我们其他的测试的路径，其他的业务可能就没有被覆盖到。       

李龙老师：这样呢，测试用例他依然没有这个思考的过程，负责第一次编写的测试人员可能有思考，但是负责执行的测试人员就没有再继续跟开发交互测试过程，没有更深入的思考，仅仅是按照用例的执行。那这种效果呢，其实是等于走过场的。           

李龙老师：再给大家举个简单例子，就像我们去测试路由器一样。比如说开启路由器设备，然后通过浏览器正确登录到软件的管理界面。这些其实在思维导图设计系统里面，他是不必要展示的一个步骤。因为我们做测试的都已经很熟悉这个业务了，测试人员应当更加关注的是开发是否做了正确的功能，功能是否做了正确的事情，而事情又是否达到了预期的效果，也就是这三个方面。因为测试人员的时间是有限的，不要过分陷入步骤的一些细节里面去探究，而是要把重点的思路放在运用到哪些测试方法上，和如何组合更加有效的覆盖率和更高的测试场景中。            

#### 基于脑图的测试设计和分析 

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-36.jpg)          
李龙老师：接下来我就和大家谈谈探讨一下脑图的一些好处，就像上面第一个图片给大家贴出来的，就是利用思维导图来做的一些方面的一些工作。因为就在整个测试过程中引入了思维导图之后，能够很大程度的提高测试人员对于需求和产品的学习和理解能力。通过使用脑图也可以进行测试分析和产品的测试分析。分析结果具有很强的条理性，并且在一定程度上，他会增强测试人员对产品理解的深度和整体的一个把控能力。         

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-7.jpg)            
李龙老师：现在咱就直接进入正题给大家直接贴图，是基于脑图的操作设计和分析的两个中心。首先这两个中心，一个是需求分析的中心，还有一个是模块用例的分析。如上面图一样，对于明确的需求，咱先聊一下需求分析这一块。对于明确的需求，参考的指标可能主要是一些软件开发的合同、项目开发的计划、系统或者子系统的设计文档、软件需求规格和说明书，当然还可能包含接口需求规格说明、用户的需求说明书和软件设计说明，还有一些继承的一些其它的一些需求，这是软件的明确需求，也就是我们需求分析里面的第一部分。          

李龙老师：需求分析的第二个问题，就是继承需求。对于继承需求，我们主要考虑的是该项目或者产品的上游内容，他应该是已经有需求或者指标了，而这一块往往是最容易忽略的地方。所以我单独拿出来和大家分享一下，做一下统计分析。正值在做项目之前，我们已经有过一个版本的存在，并且经过了大量的测试与实践，也进行了各种修改以及需求的完善。那么我们在设计本项目需求分析属性的时候，就应该继承上一版本的可用需求或者指标。以此来避免只是针对本项目的明确需求分析不到位，导致项目质量不过关。所以，对于基层需求方面主要参考的指标，我也大体的，总结了一下可以给大家说说。           

李龙老师：继承需求的一个是相关产品或者是上一个版本的软件需求规格说明书、相关产品或者是上一版本的测试需求或者是测试报告，还有一个就是在使用过程中遇到并且需要解决的一些问题的汇总，都可以放到我们的继承需求里面去。       

李龙老师：需求分析的第三个点就是隐含的需求。隐含需求，他的指标主要是对需要有十分有经验的一些测试的设计人员的一些思考，要对这个项目或者产品非常的熟悉，甚至对该产品所属行业精细明了。主要参考内容可能就是说产品的使用场景的一些数据的梳理，或者是该产品或者该项目在相关的一些行业的一些标准。还有一些就是非专业人士可能不清楚的它没有写到我们的软件需求里面那些内容，比如说一些六性要求，稳定性要求，这样的要求，虽然说一些性能的要求。          

李龙老师：刚才我分享的一块，主要是对于用脑图设计测试用例的两个中心，其中的需求分析的这么一个中心的三块内容。     

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-8.jpg)      
李龙老师：大家可以看一下这个例子，我是按照一款路由器设备的一个测试，因为它包含软硬件相关的一些内容，把他的明确需求、隐含需求等内容和大家做一个分享，大家可以看看。            

#### 基于脑图的测试用例设计             

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-9.jpg)         
李龙老师：另一个中心就是测试用例分析这么一个中心，也就说是模块用例的分析。给大家贴了一张图，基本上我是分了六块，也就是安全性、功能性、性能、稳定性、兼容性和安全性这六个部分，来和大家做一个分享。             

李龙老师：因为为了保证用例设计的完整性和高效性，采取的基本思想也是从点到面的脑图探索的方式。经过我们不断的探索和实践，脑图的第一层级使用测试类型划分应该是最理想和高效的。所以我的建议或者我的经验是不论什么产品，第一层级的内容大体是一致的。那么一个项目基本的用例分析的第一层级的结构，刚才给大家说了一下，主要是安全性、功能性、稳定性、兼容性、安全性等。当然我们根据实际项目的一些规模或者产品的属性，测试类型的可以进行适当的修改。         

李龙老师：但是，切记不要为了节省工作量或者是利于测试，而非理由的删除重要的测试类型。正如我之前就遇到过一个测试项目，由于只是进行功能的升级，为了节约项目周期，测试也没有据理力争，把稳定性的这么一个测试类型的进行了删减，结果项目上线后，由于长期运行而导致出现内存溢出的这么一个重大的缺陷。       

李龙老师：这是一个最大的血的教训，因为内存内存溢出导致整个系统给崩溃。从此以后，对于项目地测试类型和风险评估，我们就看得尤其的重要，这个在后面我会给大家好好的聊一下。         

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-10.jpg)         
李龙老师：大家可以看一下，我刚放的一个内容，就是对于我们的第一层级已经分好之后的第二层级的分类。拿功能性测试来做一个例子，大家可以先看一眼。对于每一个子功能，在用脑图进行设计的时候，主要依据以下的四个方面来进行编写。第一个，就是风险识别。第二个是目标和要素，第三个是测试要点，第四个就是业务场景。      

李龙老师：我能可以分别给大家去聊一下，首先就是风险识别的问题。任何项目都会有风险，那么我们就应该提前想到各种可能的风险，然后想办法去识别、解决或者是避免他。这一开始使用脑图设计时，用历史如果没有识别的风险，也不应该把这个子项给删除掉，还是应该保留的。因为这样，我们可以时刻提醒测试人员要有风险意识。另外，使用脑图设计测试用例的出发点就是要让每一个人去思考，以思考作为测试的其中一个技能点，可以更好的提高测试的质量。      

李龙老师：目标和要素这一条，此处主要是填写本子功能要达到的一个目标，或者是为了达成目标要解决的问题以及前提条件。如果这个子功能是由多个更小的模块组成的话，还要写清楚模块的情况，便于接下来设计测试用例时提供测试依据，避免遗漏。       

李龙老师：测试要点，这里是设计测试用例的主要的一个属性，要对每一个测试要点进行设计，但是并不要求设计人员把测试的步骤写得太过详细甚至可以不用去写测试步骤。我们需要做的是把测试的描述说清楚，我们要验证什么要做什么，我们目标是什么就可以了，而具体的就有测试的执行人员去进行。       

李龙老师：但是为了避免测试遗漏，我们需要在测试描述中写清楚测试项所采用的测试方法，比如说基本的边界值或者是等价类的一些设计方式，然后还要描述清楚该模块正常执行和异常执行下不同的一个结果反馈。       

李龙老师：最后一个方面就是业务场景。业务场景，此处主要是对功能点的一个贯穿。我们使用场景法来进行测试的设计时，尽量设计尽可能少的业务场景，把本功能的所有功能点都给贯穿进去，保证基本的业务流是可以使用的。       

李龙老师：同时整个功能性测试设计层级中有一个业务总场景，目的就是把测试产品的整个业务线连起来做一次较全面的测试，场景的数量要尽量少但是还是要精练，要把各个的要素、节点都包含进去。需要注意的是，就是以上的所有的测试描述尽量的去写事实或者是预期，不要出现过多的步骤性和死的点。当然了需求明确说明的除外。这样的好处是让测试的设计者和执行者都能充分理解测试的内容，并且给足他们测试方法或要素等的提示。避免了测试不全也杜绝了本应让自动化工具执行的一些重复性的工作，这一点应该是很重要的。我们在写功能测试的时候，主要是把我们大体的想法、步骤、思路写清楚就可以了。在这里面设计尽量不要出现太细的一些测试步骤，比如说第一步第二步第三步，这些是应该在具体的测试用例或者是外包测试里面才需要着重处理的。       

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-11.jpg)       
龙老师：大家可以看我上面那个截图还是按照路由器的那个案例给大家介绍的，对路由器产品进行设计和分析。首先就是根据需求说明书填写了该项目的明确的需求点，然后根据路由器的行业的标准和测试经验填写了隐含的需求点以及旧版本的继承需求点，并对各个需求点进行了细化。在项目用例分析中，我们对路由器的功能、性能、稳定性、兼容性和安全性的都进行了一一的分析，并且分别写出了各测试性的一些测试点。以上内容填写完成之后，我们就把脑图的左侧的项目需求点与右侧的分析就做了一一的关联，这样就避免了测试覆盖率不达标的问题。另外也可以给相关的关键点或者是指标增加相应的标识，脑图中有很多形形色色的图标，或者是标签，大家在使用过程当中可以研究一下。上面的图最终完成了测试用例设计的一部分的内容，看着会有很多连线，但是我们可以把连线给他折叠起来，其实看着还是比较清晰的，因为每一个需求点的都会与用例设计中的某个点做n对m的一个对应关系。      

李龙老师：刚才那说了这么多，把用脑图设计测试用例的两个主要的中心给大家说了一下，但是他会有很多的一些测试设计的一些要点的分析，我再给大家好好的分析一下。          

#### 测试设计要点分析   

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-12.jpg)       
李龙老师：这里再重复一下，大家可以看看上面的图片，脑图的分级主要分为左右两个半边，大家应该都很清楚了。然后分别又进行了级别的划分，左半部分就是需求的分析，主要是三个方面，明确的需求、继承需求和隐含需求，这些都比较容易理解和填充。在这里就不做过多的一个探讨，下面主要是进行测试用例设计的分级问题的一些说明。项目测试用例设计的分级主要是三级，刚才也给大家大体说一下，第一级就是按照测试类型来进行划分，划分的六个点就不给大家说了。当然，我们根据不同的被测系统特点，测试类型可以有所不同，但是需要慎重的考虑系统的各个方面，不要有遗漏。对于功能性需求，涉及面广的一定要严格区分出来，并且要特别重视异常测试的问题。      

李龙老师：第二级是该级别主要是按照需求点或者是测试点来进行划分，一般可以划分成多个测试点。第三级需求就是如果测试点可以细分到测试子项的话，就可以把测试子项作为第三级，否则直接在测试点后面写用例分析就可以了。对于功能测试下的分级，分级情况主要考虑的是风险识别、目标要素、测试要点和业务场景的内容，每个内容都不应该为空。如果实在在该地方没有什么可写的那种，可以暂时写无，待后续不断的完善测试用例时再进行补充。      

李龙老师：这个地方在脑图设计的时候，两个半边再给大家再好好的谈一下。我们左半部分一定是和需求对应的，和功能点去对应的。但是我们右半部分的测试用例设计的时候，它可以是一条一条的场景，一个一个的逻辑或者一个个的业务，我们一定是这种设计方法。而不是按照像十几年前二十年前做软件测试一样，用那种小菜单的模式或者小功能点的模式来进行脑图的设计、测试，因为他小菜单和小功能点会牵扯到很多的逻辑性的一些失真，这个误区是非常大的。         

#### 用例分析模块的六要素 

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-13.jpg)     
李龙老师：下面我和大家好好的谈一下测试用例分析模块的六个要素，也就是说相当于就是安全、功能、性能、稳定，还有兼容和安全性这六个方面，每个方面和大家进行一个简短的探讨。      

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-14.jpg)      
李龙老师：首先我们来讨论一下安装性的一个要点分析。安装性测试与EM性测试的质量自特性和可移植性的是相对应的，安装性测试主要有两个目的，第一个就是确保该软件在正常情况和异常情况这个不同条件下都可以进行正常的安装。比如我们进行首次安装、升级，完整的或者是自定义安装的时候都能够进行安装成功，完整的或者自定义的卸载都能够进行卸载成功。异常情况就包括磁盘空间不足，缺少目录创建权限等情况也都能正常的处理或者是响应。     

李龙老师：第二个目的就是何时软件在安装后是否可立即正常运行，这种通常是指运行大量的功能测试它所制定的测试用例。安装测试主要包括测试的安装代码以及安装的手册，安装手册提供如何进安装；安装代码提供安装的一些程序是否能够正常正确的运行基础数据，主要涵盖安装、升级和卸载这几个方面。可能它所牵扯的就是安装程序、基础数据配置文件，或者是如何安装、如何升级、如何卸载，以及我们的选择安装、默认安装、缺省安装等等一些要素。      

李龙老师：其实刚才我这样一聊安装测试，可能大家就能感觉到了。在用这种方法设计的时候他已经脱离了我们被测产品本身的功能项，然后我们其实写的是我们的软件测试的业务流程，只是说我们要把左半部分的需求分析里面的功能项和我们的业务流程进行对接而已，所以这是两个不同的思路。我相信很多的测试工程师他在写测试用例的时候，他是按照需求点往里面一个个去对应，但是用脑图的方式是先去梳理逻辑业务，然后去反推过来去把左半部分的需求点明确的、继承的、还是行业的那些需求点去往右半部分去对去靠拢，这是两个截然不同的一个模式。     

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-15.jpg)       
李龙老师：我们用例分析的第二条就是功能性测试，主要考虑的就是功能测试、用户需求，当然对于内部逻辑，那是另一个方面，我们在这里不做探讨。功能性主要与适应性、准确性，功能的异同性、成熟性、可靠性，或者是说他的移植性方面的质量自特性的是有一定的对应关系的。    

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-16.jpg)     
李龙老师：第三个就是性能的用例分析。他是与时间特性和资源利用效率方面的质量自特性也就是软件的质量自特性是做一一对应。性能测试可以通过手工或者是自动化的方式来模拟多种的正常、峰值以及异常的一些负载条件来对系统的各项子功能、性能指标进行测试，主要包括的方面我相信大家也都很清楚，因为都是测试工程师也都做了很长时间了，主要包括的压力测试、负载、资源利用率、基准测试以及时间特性测试方面那些。当然了这些测试类型可以单一的，或者是可以结合相关的一些其他的方法进行测试，从而有效的确认系统各指标是否符合规格的需求。     

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-17.jpg)     
李龙老师：还有一个方面是稳定性相关的，稳定性测试它是与准确性，还有成熟度、容错性以及易恢复性的一些软件质量的一些自特性做对应，他主要是测试系统的长期的稳定的运行的能力。在系统运行过程中对系统进行施压，观察系统的各种性能指标以及服务器的指标，测试系统在峰值或者是异常时能否及时的容错、恢复处理的能力，主要包括就是我截图给大家看的一个是疲劳强度的测试、容错性的测试，还有易恢复性的测试相关的内容。     

李老师：我看了群里还在一直不断的加人，之前没听着到时候可以回放一下语音，大家可以一块儿去听一下。现在是二百五十六正好是一个吉祥的数字256，比一开始我刚进来的时候二百五这个数字好听多了。      

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-18.jpg)       
李龙老师：我们用例分析的第五点，也就是兼容性这一块儿，其实是很重要的。它包括三方面内容，但是很多测试工程师他会抛弃掉两部分，一个是硬件平台，一个是操作系统。大部分人主要是以应用层的相关的一些兼容性为主导，但是其实兼容性测试的合适测试对象，他是在不同的软件和硬件配置中进行相关的运行的。在大多数的生产环境中，尤其是客户机工作站、网络连接还有数据库服务器等连接的方面，具体的硬件规格是有所不同的。客户机工作站可能会安装不同的软件，比如说应用系统、应用程序、驱动程序，这些在任何时候都可能运行许多不同的软件组合，从而占用不同的资源。在进行兼容性测试时，我们就要考虑产品运行的不同的硬件的平台的兼容性。       

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-19.jpg)      
李龙老师：用例分析的最后一个模块就是安全性测试，大家可以看那个图片。安全性测试，它是对应用程序的安全服务和潜在的安全性缺陷的验证，他的范围就很广了，当然了一个较完整的安全性测试需要包括以下的几个类型：一个就是平台的安全性；还有就是业务安全性；还有就是license的安全性，也就是他的注册码，license相关的一些验证；还有web安全性；DDos就是抗拒服务攻击的能力；还有自动化工具扫描，他扫描出来一些比如说端口安全，还有一些注入的安全，这么一些内容。       

李龙老师：目前几乎没有可用的工具来彻底的测试各种安全性的测试类型，因为程序中的功能错误了也可代表潜在的安全性缺陷，因此在实施安全性测试以前需要实施功能测试。那么作为安全性测试人员，或者设计人员需要注意的就是安全性测试并不是最终证明应用程序是安全的，而只是用验证所设立对策的有效性，而这些对策的就是基于威胁分析阶段所做的假设而选择的。一个好的安全测试工程师或者是渗透测试工程师，他是要先猜错，先试错，就是我先猜测或者认为你这里有问题，然后我去试图去突破或者是攻击你这个问题，这样来进行安全性测试。      

李龙老师：我们举个例子，比如说，如果保险银行系统出现漏洞，那么可能直接导致上千万甚至上亿的资金被盗用。如果登录或者是权限划分的模块出现漏洞，攻击者就可以在你的系统中来去自如，甚至可以对你的服务器进行任何的操作。当服务器受到ddos等洪水攻击的时候，最直接现象就是服务器死机，宕机或者是拒绝服务。当然像公司的门户网站，我们如果受到攻击的话也会很有可能会对公司的名誉、产品产生不良的影响，使客户对我们失去信心。所以安全性的问题还是尽量的早发现早解决，因为一旦漏洞公布于世，再解决的话就已经不是成本的问题了。      

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-20.jpg)       
李龙老师：其实给大家聊到这里，我基本上就把利用思维导图设计测试用例的一个大体的框架，还有他的一些要素给大家做了简单的介绍。现在可以给大家的一块再去总结一下或者梳理一下，那就是我们左右两半部分那是缺少不了的，就是需求分析和这个模块的用例分析两个阶段。在需求分析里面，他的明确的需求、继承的需求和隐含的需求，这三块是我们可以在进行测试设计的时候是可以找相关的产品经理、项目经理甚至说研发去获取到的。        

李龙老师：我们在做用例分析的时候，我们所分别去罗列的六个层级或者是六个测试类型的分类，这个基本上就把所有的一些软硬件的一些甚至说是还有和平台相关的测试的一些覆盖方面内容都已经涵盖进去了，而这些恰恰又与需求分析里面的那三项需求的点作了相关的一些对应关系和覆盖率。以这种方式，我们就把整个的产品，软件产品也好，硬件产品也好，软硬件也好，就结合在一起，而真正的实现了把测试的覆盖率提高到最优化的状态。          

李龙老师：好处当然也有很多，比如说我们再去设计测试用例的时候，我们可以使用思维导图这么一个软件。然后把测试用例、步骤尽量的简化，把描述、需求、目标尽量的详细化或者是说业务流程化，让测试的具体的执行人员再去执行的时候可以有一定的发挥，不会变成一百个人执行一个测试用例最后只能有一条路径就往下执行，那说实话是真的是把测试工程师当成了机器来使了。我相信大家也很清楚，以后的人工成本的话可能会很贵，但是如果不会做自动化测试的人，它的成本可能就很低了。           

#### 使用场景注意事项     

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-21.jpg)       
李龙老师：我们现在可以谈一下思维导图设计测试用例的一个场景的注意事项，因为脑图最大的好处就是其放射性思考与人脑的思维模式是非常接近的。他是一种发展的设计方法，所以我们在使用该方法设计测试用例的时候，必须对需求很清晰，或者是说测试人员需要在项目中提前介入。主要遵守的一些原则，主要包括这么几个方面吧，我和大家聊一下。      

李龙老师：第一个就是从项目开始阶段介入，参与需求分析，记录需求的一些要点。还有就是在全程软件测试中，软件测试人员应该从需求阶段开始进来参与，一起对功能点进行评估，消除模糊性的一些疑点，将明确的需求点和不明确的需求点都记录到脑图中的左半部分的需求分析中，作为脑图右半部分测试用例的一些思考的来源，当然这个要与产品、开发人员要达成一致的意见。          

李龙老师：在研发过程中测试人员可以根据原型图设计脑图的用例，没有实际的系统，测试其实也可以先提前进行的，对吧。因为我们作为测试工程师来说的话，其实大部分时间都是在设计测试的案例。我们去与开发人员进行查漏补缺，做一些用例评审，这是一点儿问题都没有的。主要就是为了确认测试的功能点、测试的场景以及测试数据的准备情况。这几个方面呢，他不可能一开始就没有下来，但是一定要不断的沟通、挖掘，然后也在不断的去完善脑图的这么一个用例设计的相关内容。          

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-22.jpg)        
李龙老师：当然了，还有一些情况是不推荐使用本方法做这个用例分析的。因为就像一开始我刚和大家分享的时候，传统的测试用例编写对于用例的描述和步骤的要求过高。在现今的软件行业发展的规模下，会让测试的设计人员疲于编写测试步骤，然后再重构再修改浪费了很多时间，也让测试用例失去了一些灵活性。而使用思维导图设计测试用例，从大脑的思维方式出发，循序渐进的设计出测试用例，会让每一个测试的执行人员跟着测试者的思路去走，提高了测试人员的积极性，并且在测试过程中，会不断增加新的思路，避免了死用例和死循环。          

李龙老师：还有一点就是脑图测试用例的重点他不是写测试的步骤，而是测试的描述或者思路，这样会让每一个人测试的步骤不尽相同，但是测试点的目标是相同的，保证了测试的高效性也避免了重复的工作量。         

李龙老师：上面那种主要给大家介绍的就是基于脑图实现测试设计与分析的一些内容和在实际案例中的一些使用，现在的回归正题，就是说到底是哪些情况不推荐使用。一个就是说的就是抱着通过思维导图设计能够把需求覆盖到百分之百，场景覆盖百分之百，甚至bug为零。当然了，我们虽然经过了这种测试的一个探讨。经过验证，那测试其实也永远达不到以上的三个目标，不光是使用思维导图达不到，用任何一个方式也都不可能把bug消灭为零这么一个状态。我们的目标只能是尽量趋近于这个目标，并且就像刚才说的我个人认为就是任何的测试设计方法都不可能达到缺陷率为零。          

李龙老师：对于业务不熟悉或者是无法设计出合适的测试场景的，并且测试执行人员也很难理解的情况下，也可能不太适合做这种测试用例。         

李龙老师：如果我们要是通过外包测试的话，就需要详细的一些测试用例的执行步骤，测试报告，而这个情况下，因为思维导图他的重点不是去完成具体的测试步骤，所以不建议采用这个方法。但是我们可以试图让测试执行人员或者是想学习测试设计人员根据脑图的用例设计的内容填写标准的测试用例，从另一个层面可以提高或者是消除测试设计人员以外的其他人员的工作积极性和自主能动性，这其实是何乐而不为的一个事情，对于产品研发和测试呢，没有沟通或者是研发完成交付测试才能介入情况下也不建议采取这种方式。           

李龙老师：基于脑图实现测试设计与分析的使用，就是不仅对测试自身的素质要求高，对研发要求也高，不单单要有相关的测试经验，而且要有相关的开发经验，可以理解开发过程中遇到的问题，甚至有时候我们需要深入到开发代码中去排查。还有一点就是使用这种设计方法的公司——项目管理流程可能是比较清晰的，脑图设计也要从项目的开始就要进行让测试介入，这样才能把测试的场景和思维捋顺，提高测试对产品的质量保证。           

李龙老师：以上差不多聊了一个小时了，主要给大家把使用思维导图做测试的设计以及使用思维导图做设计的时候的一些框架图给大家做了一个分析，大家可以在实际工作的时候去使用一下。如果有需要的朋友呢，也可以通过Mango或者是通过我把思维导图的这个模板发给大家。           

#### VIPTest活动介绍       

![](\img\in-post\post-test-base\2018-12-02-TestCaseHowToDesign-23.jpg)         
李龙老师：最后一个图就是感谢VIPTest,然后做了一些沙龙，然后今天有幸能和大家一块进行一个分享。咱这个群里好像有好多人。都是半路杀进来的，我也不知道大家有没有听清楚或者听明白，有什么问题我们现在也可以一块儿交流一下。     

李龙老师：我看到小木木的向日葵说外包测试是什么？我不知道你问的这句话是什么含义，你是问测试外包吗，就是我们基本上就属于第三方测试，或者是说像一些大型的一些企业一些集团，比如说像太平保险、用友还有浪潮。这些公司他们内部可能养不了太多的一些测试工程师，他会把很多的测试任务包给其他的企业其他测试工程师或者其他的一些测试团队去进行验证测试，这个方式属于测试外包。        

李龙老师：呼叫一下我们说话很嗲嗲的Mango美女，今天我的分享差不多已经结束了，说实话我分享这个的时候也是比较担心的，因为设计测试用例的这么一个方式或者这个课题是比较枯燥的，而且所有人都感觉自己会，但是每个人的方式都不一样，我今天是把我设计测试用例或者是这十多年的一个经验给大家做了一个分享。        

李龙老师：在这个里面可能大家也能感觉出来，我没有和大家去聊太多的高大上的一些案例或者是一些内容。其实因为也没有这个必要，因为我们都是做软件测试的，如果说和大家聊物联网的测试，聊大数据的测试，聊工具的测试这些内容可能大家感兴趣，但是大家千万不要忘了，我们软件测试的初衷就是为了消灭缺陷，我们要从一开始的业务就开始来努力。          

李龙老师：不忘初心，不忘自己的目标，把软件测试的设计，把他的覆盖率提高，把设计的效率提高，用这个方法的话，我是感觉还是比较不错的。       

李龙老师：就像今年10月份在北京参加VIPTEST举办的还有他最近举办的中国首届互联网测试大会一样，朱教授说的那句话一样，软件测试我们从哪里来到哪里去，这么一个哲学问题。那就是我们做软件测试的测试用例，需求从哪里来，我们如何去设计，我们设计出来之后如何去执行。在这个方面，我希望今天的分享能够带给大家一些启示，就已经很高兴了。