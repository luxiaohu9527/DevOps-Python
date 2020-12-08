
// 公共
def registry = "harbor.akcops.com"

// 项目
def project = "qtt-java-cloud"
def job_name = "${app_name}"
def image_name = "${registry}/${project}/${job_name}:${BUILD_NUMBER}"
def git_address = "${git_address}"

// 认证  
// def secret_name = "test1-secret"
def docker_registry_auth = "0c72ff5d-decc-4224-8593-c178afc25629"
def git_auth = "1232850e-a124-4d09-82b6-c9687103f957"
def k8s_auth = "c94dd7a4-7be0-4399-8f86-979941a03c75"

timeout(time: 1000, unit: 'SECONDS') {
podTemplate(label: 'jenkins-slave', cloud: 'kubernetes', containers: [
    containerTemplate(
        name: 'jnlp',
        image: "${registry}/library/jenkins-slave-jdk:1.8"
    ),
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
    hostPathVolume(mountPath: '/usr/bin/docker', hostPath: '/usr/bin/docker')
  ],
)

{
  node {
      // 第一步
      stage('拉取代码'){
         echo "Git 阶段"
         checkout([$class: 'GitSCM', branches: [[name: '${Branch}']], userRemoteConfigs: [[credentialsId: "${git_auth}", url: "${git_address}"]]])
         echo "+++++++++++++++++++代码拉取完成+++++++++++++++++++++++++"
      }

      // 第二步
      stage('Sonar扫描'){
         echo "+++++++++++++++++++Sonar扫描完成+++++++++++++++++++++++++"
      }
      
      // 第三步
      stage('代码编译'){
            sh "mvn clean package -Dmaven.test.skip=true"
          echo "+++++++++++++++++++代码编译完成+++++++++++++++++++++++++"
      }
      
      // 第四步
      stage('War包处理'){
            sh "/opt/script/cloud-tomcat-k8s.sh"
          echo "+++++++++++++++++++War处理完成+++++++++++++++++++++++++"
      }
      
      // 第五步
      stage('构建镜像'){
          withCredentials([usernamePassword(credentialsId: "${docker_registry_auth}", passwordVariable: 'password', usernameVariable: 'username')]) {
            commitId = sh(script: 'git log --pretty=format:"%h" -1', returnStdout: true).trim()
            nsName = sh(script: "echo test1", returnStdout: true).trim()
            secret_name = sh(script: "echo ${nsName}-secret", returnStdout: true).trim()
            
            sh """
              echo '
                FROM harbor.akcops.com/library/akc-dev-tomcat-template:1.0
                RUN rm -rf /usr/local/tomcat/webapps/*
                COPY ${job_name}.war /mnt/
                COPY setenv.sh /usr/local/tomcat/bin/
                RUN unzip -o /mnt/${job_name}.war -d /usr/local/tomcat/webapps/ROOT
              ' > Dockerfile
              docker build -t ${image_name}-${commitId}-${VERSION}-${ENV} .
              docker login -u ${username} -p '${password}' ${registry}
              docker push ${image_name}-${commitId}-${VERSION}-${ENV}
              docker rmi ${image_name}-${commitId}-${VERSION}-${ENV}
              echo "nsName=$nsName"
              sh /opt/script/k8s-check-ns.sh $nsName ${registry} ${username} ${password}

              """
          echo "+++++++++++++++++++构建镜像完成+++++++++++++++++++++++++"
        }
      }

      // 第六步
      stage('部署K8S平台'){
      // 使用 Kubectl 的方法，提供 Kubernetes环境，在其方法块内部能够执行 kubectl 命令
        healthPath = sh(script: "python /opt/script/cmdbGetHostIpHealth.py ${app_name}", returnStdout: true).trim()
        // nsName = sh(script: "echo test1", returnStdout: true).trim()
        // commitId = sh(script: 'git log --pretty=format:"%h" -1', returnStdout: true).trim()
        
        sh """
          echo 'healthPath='$healthPath
          echo 'nsName='$nsName
          echo 'commitId='$commitId
          cp /opt/script/deploy.yml .
          rm ${job_name}.war
          sed -i 's#IMAGE_NAME#${image_name}-${commitId}-${VERSION}-${ENV}#' deploy.yml
          sed -i 's#ENV#${ENV}#' deploy.yml
          sed -i 's#APP_NAME#${job_name}#' deploy.yml
          sed -i 's#SECRET_NAME#${secret_name}#' deploy.yml
          sed -i 's#NAMESPACE#${nsName}#' deploy.yml
          sed -i 's#HEALTH_PATH#${healthPath}#' deploy.yml
          sh /opt/script/k8s-check-isdp.sh ${nsName} ${job_name}
          sleep 5
          kubectl apply -f deploy.yml 
          """
        echo "+++++++++++++++++++部署K8S平台完成+++++++++++++++++++++++++"
      }
     
      // 第七步   
      stage('应用健康检查'){
		// 设置检测延迟时间 10s,10s 后再开始检测
		sleep 5
		timeout(time: 5, unit: 'MINUTES') { sh "/opt/script/k8s-health.sh ${app_name} ${nsName}" } 
// 		sh "/opt/script/k8s-health.sh ${app_name} ${nsName}"	
      }         
    }
 
 }
}
